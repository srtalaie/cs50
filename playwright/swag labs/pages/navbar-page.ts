import { expect, type Locator, type Page } from '@playwright/test'

export class NavBar {
  readonly page: Page
  readonly appLogo: Locator
  readonly burgerMenu: Locator

  constructor(page: Page) {
    this.page = page
    this.appLogo = page.locator('.header_label').locator('.app_logo')
    this.burgerMenu = page.locator('#menu_button_container').locator('.bm-burger-button').getByRole('button')
  }

  async verifyAppLogo() {
    await expect(this.appLogo).toHaveText('Swag Labs')
  }

  async verifyBurgerMenuItems() {
    await this.burgerMenu.click()

    // Verify nav items
    const burgerMenuNavItem = this.page.locator('.bm-item-list > a')
    await expect(burgerMenuNavItem).toHaveText(['All Items', 'About', 'Logout', 'Reset App State'])

    // Close nav menu
    const burgerMenuCloseBtn = this.page.locator('.bm-cross-button').locator('#react-burger-cross-btn')
    await burgerMenuCloseBtn.click()
  }
}