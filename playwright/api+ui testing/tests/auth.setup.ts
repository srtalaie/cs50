import { test as setup } from '@playwright/test'
import path from 'path'

const authFile = path.join(__dirname, '../playwright/.auth/user.json')

const creds = {
  email: process.env.EMAIL as string,
  password: process.env.PASSWORD as string,
}

setup('Log in', async ({ page, baseURL, request }) => {
  await page.goto('/')

  await page.getByPlaceholder('Email').fill(creds.email)
  await page.getByPlaceholder('Password').fill(creds.password)
  await page.locator('#submit').click()

  await page.waitForURL(`${baseURL}/contactList`)

  await page.context().storageState({ path: authFile })
})