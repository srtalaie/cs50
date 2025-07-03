import { faker } from '@faker-js/faker'
import { expect, test as setup } from '@playwright/test'
import path from 'path'
import { user } from '../types'

const authFile = path.join(__dirname, '../playwright/.auth/user.json')

const new_user: user = {
  firstName: faker.person.firstName(),
  lastName: faker.person.lastName(),
  email: faker.internet.email(),
  password: faker.internet.password(),
}

setup('create user and authenticate', async ({ page, baseURL, request }) => {
  // Create the new user through the API
  const response = await request.post(`${baseURL}/users`, {
    headers: {
      'Content-Type': 'application/json'
    },
    data: new_user,
  })

  const data = await response.json()

  expect(response.status()).toBe(201)
  expect(data.user.firstName).toBe(new_user.firstName)

  // Log in with newly created user
  await page.goto('/')

  await page.getByPlaceholder('Email').fill(new_user.email)
  await page.getByPlaceholder('Password').fill(new_user.password)
  await page.locator('#submit').click()

  await page.waitForURL(`${baseURL}/contactList`)

  await page.context().storageState({ path: authFile })
})