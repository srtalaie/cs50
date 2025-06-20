import { type Locator, type Page } from '@playwright/test'

export class InventoryPage {
  readonly page: Page
  readonly appLogo: Locator
  readonly pageTitle: Locator
  readonly inventoryItemList: Locator
  readonly productSort: Locator
  readonly shoppingCart: Locator
  readonly burgerMenu: Locator

  constructor(page: Page) {
    this.page = page
    this.appLogo = page.locator('.header_label').locator('.app_logo', { hasText: 'Swag Labs' })
    this.pageTitle = page.locator('.header_secondary_container').locator('.title', { hasText: 'Products' })
    this.productSort = page.locator('.right_component').locator('.product_sort_container')
    this.shoppingCart = page.locator('.shopping_cart_container').locator('.shopping_cart_link')
    this.burgerMenu = page.locator('#menu_button_container').locator('.bm-burger-button').getByRole('button')
  }
}