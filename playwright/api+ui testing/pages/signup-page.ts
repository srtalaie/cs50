import { expect, type Locator, type Page } from '@playwright/test'

export class SignUpPage {
  readonly page: Page
  readonly addUserHeading: Locator
  readonly instructions: Locator
  readonly firstNameInput: Locator
  readonly lastNameInput: Locator
  readonly emailInput: Locator
  readonly passwordInput: Locator
  readonly submitBtn: Locator
  readonly errorMessage: Locator
  readonly cancelBtn: Locator

  constructor(page: Page) {
    this.page = page
    this.addUserHeading = page.getByRole('heading', { name: 'Add User' })
    this.instructions = page.getByText('Sign up to begin adding your')
    this.firstNameInput = page.getByRole('textbox', { name: 'First Name' })
    this.lastNameInput = page.getByRole('textbox', { name: 'Last Name' })
    this.emailInput = page.getByRole('textbox', { name: 'Email' })
    this.passwordInput = page.getByRole('textbox', { name: 'Password' })
    this.submitBtn = page.getByRole('button', { name: 'Submit' })
    this.errorMessage = page.locator('#error')
    this.cancelBtn = page.getByRole('button', { name: 'Cancel' })
  }

  async goTo() {
    await this.page.goto('https://thinking-tester-contact-list.herokuapp.com/addUser')
  }

  async verifyPageElements() {
    await expect(this.addUserHeading).toBeVisible()
    await expect(this.instructions).toBeVisible()
    await expect(this.firstNameInput).toBeVisible()
    await expect(this.lastNameInput).toBeVisible()
    await expect(this.emailInput).toBeVisible()
    await expect(this.passwordInput).toBeVisible()
    await expect(this.submitBtn).toBeVisible()
    await expect(this.cancelBtn).toBeVisible()
  }

  async cancel() {
    await this.cancelBtn.click()
    await expect(this.page).toHaveTitle('Contact List App')
  }

  async userCreateSuccess(firstName: string, lastName: string, email: string, password: string) {
    await this.firstNameInput.fill(firstName)
    await this.lastNameInput.fill(lastName)
    await this.emailInput.fill(email)
    await this.passwordInput.fill(password)
    await this.submitBtn.click()

    await expect(this.page).toHaveTitle('My Contacts')
  }

  async userCreateFailureFirstName(lastName: string, email: string, password: string) {
    await this.lastNameInput.fill(lastName)
    await this.emailInput.fill(email)
    await this.passwordInput.fill(password)
    await this.submitBtn.click()

    await expect(this.errorMessage).toHaveText('User validation failed: firstName: Path `firstName` is required.')
  }
  async userCreateFailureLastName(firstName: string, email: string, password: string) {
    await this.firstNameInput.fill(firstName)
    await this.emailInput.fill(email)
    await this.passwordInput.fill(password)
    await this.submitBtn.click()

    await expect(this.errorMessage).toHaveText('User validation failed: lastName: Path `lastName` is required.')
  }
  async userCreateFailureEmail(firstName: string, lastName: string, password: string) {
    await this.firstNameInput.fill(firstName)
    await this.lastNameInput.fill(lastName)
    await this.passwordInput.fill(password)
    await this.submitBtn.click()

    await expect(this.errorMessage).toHaveText('User validation failed: email: Email is invalid')
  }
  async userCreateFailurePassword(firstName: string, lastName: string, email: string) {
    await this.firstNameInput.fill(firstName)
    await this.lastNameInput.fill(lastName)
    await this.emailInput.fill(email)
    await this.submitBtn.click()

    await expect(this.errorMessage).toHaveText('User validation failed: password: Path `password` is required.')
  }

  async userCreateFailureAll() {
    await this.submitBtn.click()

    await expect(this.errorMessage).toHaveText('User validation failed: firstName: Path `firstName` is required., lastName: Path `lastName` is required., email: Email is invalid, password: Path `password` is required.')
  }
}