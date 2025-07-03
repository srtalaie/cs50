import { faker } from '@faker-js/faker'
import { test } from '@playwright/test'
import { SignUpPage } from '../pages/signup-page'
import { user } from '../types'

const new_user: user = {
  firstName: faker.person.firstName(),
  lastName: faker.person.lastName(),
  email: faker.internet.email(),
  password: faker.internet.password(),
}

test.describe('Sign Up page tests', () => {
  let signUpPage: any

  test.beforeEach(async ({ page }) => {
    signUpPage = new SignUpPage(page)
    await signUpPage.goTo()
  })

  test('Verify page elements', async () => {
    await signUpPage.verifyPageElements()
  })

  test.describe('Error messages display correctly', () => {
    test('Error message for all empty fields', async () => {
      await signUpPage.userCreateFailureAll()
    })
    test('Error message first name empty field', async () => {
      await signUpPage.userCreateFailureFirstName(new_user.lastName, new_user.email, new_user.password)
    })
    test('Error message last name empty field', async () => {
      await signUpPage.userCreateFailureLastName(new_user.firstName, new_user.email, new_user.password)
    })
    test('Error message email empty field', async () => {
      await signUpPage.userCreateFailureEmail(new_user.firstName, new_user.lastName, new_user.password)
    })
    test('Error message password empty field', async () => {
      await signUpPage.userCreateFailurePassword(new_user.firstName, new_user.lastName, new_user.email)
    })
  })

  test('Cancel button returns user to homepage', async () => {
    await signUpPage.cancel()
  })

  test('Sign Up success', async () => {
    await signUpPage.userCreateSuccess(new_user.firstName, new_user.lastName, new_user.email, new_user.password)
  })
})