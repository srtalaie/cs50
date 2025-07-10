import { faker } from "@faker-js/faker"
import { APIRequestContext, request, test } from "@playwright/test"
import { HomePage } from "../pages/home-page"
import { contact } from "../types"

// Create a date and put it in correct format
const randomDate = faker.date.between({ from: '1980-01-01', to: Date.now() })
const isoFormatted = randomDate.toLocaleDateString('en-CA', { year: 'numeric', month: '2-digit', day: '2-digit' })
const dateParts = isoFormatted.split('-')

const new_contact: contact = {
  birthdate: `${dateParts[0]}-${dateParts[1]}-${dateParts[2]}`,
  city: faker.location.city(),
  country: faker.location.country(),
  email: faker.internet.email(),
  firstName: faker.person.firstName(),
  lastName: faker.person.lastName(),
  phone: faker.string.numeric(10),
  postalCode: faker.location.zipCode('#####'),
  stateProvince: faker.location.state(),
  street1: faker.location.streetAddress(),
  street2: faker.location.secondaryAddress(),
}

test.describe('Home page tests', () => {
  let homePage: any
  let response: any
  let page: any
  let data: any
  let cookies: any

  test.beforeEach(async ({ baseURL, browser }) => {
    const apiContext: APIRequestContext = await request.newContext()
    const browserContext = await browser.newContext()

    page = await browserContext.newPage()
    homePage = new HomePage(page)

    cookies = await browserContext.cookies()

    response = await apiContext.post(`${baseURL}/contacts`, {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${cookies[0].value}`
      },
      data: new_contact
    })

    data = await response.json()
    await homePage.goTo()
  })

  test.afterEach(async ({ baseURL }) => {
    const apiContext: APIRequestContext = await request.newContext()
    const res = await apiContext.delete(`${baseURL}/contacts/${data._id}`, {
      headers: {
        'Authorization': `Bearer ${cookies[0].value}`
      }
    })
  })

  test.only('Contact Table displays info correctly', async () => {
    await homePage.contactTableCheck([new_contact])
  })
})

