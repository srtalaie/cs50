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
    await expect(this.contactTable.locator('contactTableHead').locator('td').locator('th').nth(0)).toBe('Name')
    await expect(this.contactTable.locator('contactTableHead').locator('td').locator('th').nth(1)).toBe('Birthdate')
    await expect(this.contactTable.locator('contactTableHead').locator('td').locator('th').nth(2)).toBe('Email')
    await expect(this.contactTable.locator('contactTableHead').locator('td').locator('th').nth(3)).toBe('Phone')
    await expect(this.contactTable.locator('contactTableHead').locator('td').locator('th').nth(4)).toBe('Address')
    await expect(this.contactTable.locator('contactTableHead').locator('td').locator('th').nth(5)).toBe('City, State/Province, Postal Code')
    await expect(this.contactTable.locator('contactTableHead').locator('td').locator('th').nth(6)).toBe('Country')

    // At least 1 row of contact info exists
    const rowCount = await this.contactRow.count()
    expect(rowCount).toBeGreaterThan(0)

    // Loop through all rows and verify info is correct
    for (let i = 0; i < rowCount; i++) {
      await expect(this.contactRow.nth(i).locator('td').nth(1)).toBe(`${contact[i].firstName} ${contact[i].lastName}`)
      await expect(this.contactRow.nth(i).locator('td').nth(2)).toBe(contact[i].birthdate)
      await expect(this.contactRow.nth(i).locator('td').nth(3)).toBe(contact[i].email)
      await expect(this.contactRow.nth(i).locator('td').nth(4)).toBe(contact[i].phone)
      await expect(this.contactRow.nth(i).locator('td').nth(5)).toBe(`${contact[i].street1} ${contact[i].street2}`)
      await expect(this.contactRow.nth(i).locator('td').nth(6)).toBe(`${contact[i].city} ${contact[i].stateProvince} ${contact[i].postalCode}`)
      await expect(this.contactRow.nth(i).locator('td').nth(7)).toBe(contact[i].country)
    }
  }
}