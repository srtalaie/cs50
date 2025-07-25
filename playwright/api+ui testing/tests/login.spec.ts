import { test } from "@playwright/test"
import { LoginPage } from "../pages/login-page"

test.describe('Login page tests', () => {
  let loginPage: any

  test.beforeEach(async ({ page }) => {
    loginPage = new LoginPage(page)
    await loginPage.goTo()
  })

  test('Verify all page elements exist', async () => {
    await loginPage.verifyPageElements()
  })

  test('User is able to login', async () => {
    await loginPage.loginSuccess(process.env.EMAIL, process.env.PASSWORD)
  })

  test('User gets error message when logging in with inocrrect creds', async () => {
    await loginPage.loginError(process.env.EMAIL)
  })

  test('User can successfully navigate to the sign up page', async () => {
    await loginPage.signUpPageNav()
  })
})