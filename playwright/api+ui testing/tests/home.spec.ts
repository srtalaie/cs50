import { test } from "@playwright/test"
import { HomePage } from "../pages/home-page"

test.describe('Home page tests', () => {
  let homePage: any

  test.beforeEach(async ({ page }) => {
    homePage = new HomePage(page)
    await homePage.goTo()
  })

  test('Clicking Add a new contact goes to add contact page', async () => {
    await homePage.goToAddNewContact()
  })

  test('Clicking logout takes user to main app page', async () => {
    await homePage.logOut()
  })
})

