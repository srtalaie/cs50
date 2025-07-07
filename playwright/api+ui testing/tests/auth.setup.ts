import { test as setup } from '@playwright/test'
import path from 'path'

const authFile = path.join(__dirname, '../playwright/.auth/user.json')

// const new_user: user = {
//   firstName: faker.person.firstName(),
//   lastName: faker.person.lastName(),
//   email: faker.internet.email(),
//   password: faker.internet.password(),
// }

const creds = {
  email: process.env.EMAIL as string,
  password: process.env.PASSWORD as string,
}

setup('create user and authenticate', async ({ page, baseURL, request }) => {
  // // Create the new user through the API
  // const response = await request.post(`${baseURL}/users`, {
  //   headers: {
  //     'Content-Type': 'application/json'
  //   },
  //   data: new_user,
  // })

  // const data = await response.json()

  // expect(response.status()).toBe(201)
  // expect(data.user.firstName).toBe(new_user.firstName)
  await page.goto('/')

  await page.getByPlaceholder('Email').fill(creds.email)
  await page.getByPlaceholder('Password').fill(creds.password)
  await page.locator('#submit').click()

  await page.waitForURL(`${baseURL}/contactList`)

  await page.context().storageState({ path: authFile })
})