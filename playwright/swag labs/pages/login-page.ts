import { expect, type Locator, type Page } from '@playwright/test'

export class LoginPage {
  readonly page: Page
  readonly login_logo: Locator
  readonly username_input: Locator
  readonly password_input: Locator
  readonly login_button: Locator

  constructor(page: Page) {
    this.page = page
    this.login_logo = page.locator('.login_logo')
    this.username_input = page.locator('#user-name')
    this.password_input = page.locator('#password')
    this.login_button = page.locator('#login-button')
  }

  async goTo() {
    await this.page.goto('https://www.saucedemo.com/')
  }

  async verifyPageElements() {
    await expect(this.login_logo).toHaveText('Swag Labs')
    await expect(this.username_input).toHaveAttribute('placeholder', 'Username')
    await expect(this.password_input).toHaveAttribute('placeholder', 'Password')
    await expect(this.login_button).toBeVisible()
  }
}