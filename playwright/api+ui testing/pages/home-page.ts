import { expect, type Locator, type Page } from '@playwright/test'
import { contact } from '../types'

export class HomePage {
  readonly page: Page
  readonly contactListHeading: Locator
  readonly instructions: Locator
  readonly addNewContactBtn: Locator
  readonly contactTable: Locator
  readonly contactRow: Locator
  readonly logOoutBtn: Locator

  constructor(page: Page) {
    this.page = page
    this.contactListHeading = page.getByRole('heading', { name: 'Contact List' })
    this.instructions = page.getByText('Click on any contact to view')
    this.addNewContactBtn = page.getByRole('button', { name: 'Add a New Contact' })
    this.contactTable = page.getByRole('table')
    this.contactRow = page.locator('.contactTableBodyRow')
    this.logOoutBtn = page.getByRole('button', { name: 'Logout' })
  }

  async goTo() {
    await this.page.goto('https://thinking-tester-contact-list.herokuapp.com/contactList')
  }

  async contactTableCheck(contact: contact[]) {
    await expect(this.contactTable).toBeVisible()

    // Check header row info
    await expect(this.page.getByRole('cell', { name: 'Name' })).toBeVisible()
    await expect(this.page.getByRole('cell', { name: 'Birthdate' })).toBeVisible()
    await expect(this.page.getByRole('cell', { name: 'Email' })).toBeVisible()
    await expect(this.page.getByRole('cell', { name: 'Phone' })).toBeVisible()
    await expect(this.page.getByRole('cell', { name: 'Address' })).toBeVisible()
    await expect(this.page.getByRole('cell', { name: 'City, State/Province, Postal Code' })).toBeVisible()
    await expect(this.page.getByRole('cell', { name: 'Country' })).toBeVisible()

    // At least 1 row of contact info exists
    const rowCount = await this.contactRow.count()
    expect(rowCount).toBeGreaterThan(0)

    // Loop through all rows and verify info is correct
    for (let i = 0; i < rowCount; i++) {
      console.log(`${contact[i].firstName} ${contact[i].lastName}`);

      await expect(this.page.getByRole('cell', { name: `${contact[i].firstName} ${contact[i].lastName}` })).toBeVisible()
      await expect(this.page.getByRole('cell', { name: contact[i].birthdate })).toBeVisible()
      await expect(this.page.getByRole('cell', { name: contact[i].email })).toBeVisible()
      await expect(this.page.getByRole('cell', { name: contact[i].phone })).toBeVisible()
      await expect(this.page.getByRole('cell', { name: `${contact[i].street1} ${contact[i].street2}` })).toBeVisible()
      await expect(this.page.getByRole('cell', { name: `${contact[i].city} ${contact[i].stateProvince} ${contact[i].postalCode}` })).toBeVisible()
      await expect(this.page.getByRole('cell', { name: contact[i].country })).toBeVisible()
    }
  }
}