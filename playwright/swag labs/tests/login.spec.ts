import { test } from "@playwright/test"
import { LoginPage } from "../pages/login-page"

test('Login Page', async ({ page }) => {
  const loginPage = new LoginPage(page)

  await loginPage.goTo()
  await loginPage.verifyPageElements()
})