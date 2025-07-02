import { expect, type Locator, type Page } from '@playwright/test'

export class LoginPage {
  readonly page: Page
  readonly pageHeading: Locator
  readonly loginFormHeading: Locator
  readonly emailInput: Locator
  readonly passwordInput: Locator
  readonly submitButton: Locator
  readonly signUpButton: Locator
  readonly errorMessage: Locator

  constructor(page: Page) {
    this.page = page
    this.pageHeading = page.getByRole('heading', { name: 'Contact List App' })
    this.loginFormHeading = page.getByText('Log In:')
    this.emailInput = page.getByRole('textbox', { name: 'Email' })
    this.passwordInput = page.getByRole('textbox', { name: 'Password' })
    this.submitButton = page.getByRole('button', { name: 'Submit' })
    this.signUpButton = page.getByRole('button', { name: 'Sign up' })
    this.errorMessage = page.getByText('Incorrect username or password')
  }

  async goTo() {
    await this.page.goto('https://thinking-tester-contact-list.herokuapp.com/')
  }

  async verifyPageElements() {
    await expect(this.pageHeading).toBeVisible()
    await expect(this.loginFormHeading).toBeVisible()
    await expect(this.emailInput).toBeVisible()
    await expect(this.passwordInput).toBeVisible()
    await expect(this.submitButton).toBeVisible()
    await expect(this.signUpButton).toBeVisible()
  }

  async loginSuccess(email: string, password: string) {
    await this.emailInput.fill(email)
    await this.passwordInput.fill(password)

    await this.submitButton.click()
    await expect(this.page).toHaveTitle('My Contacts')
  }

  async loginError(email: string) {
    await this.emailInput.fill(email)
    await this.passwordInput.fill('1')

    await this.submitButton.click()
    await expect(this.errorMessage).toHaveText('Incorrect username or password')
  }

  async signUpPageNav() {
    await this.signUpButton.click()

    await expect(this.page).toHaveTitle('Add User')
  }
}