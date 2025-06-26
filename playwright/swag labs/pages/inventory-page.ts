import { expect, type Locator, type Page } from '@playwright/test'

export class InventoryPage {
  readonly page: Page
  readonly appLogo: Locator
  readonly pageTitle: Locator
  readonly inventoryItemList: Locator
  readonly inventoryItem: Locator
  readonly productSort: Locator
  readonly shoppingCart: Locator
  readonly shoppingCartBadge: Locator
  readonly burgerMenu: Locator

  constructor(page: Page) {
    this.page = page
    this.appLogo = page.locator('.header_label').locator('.app_logo')
    this.pageTitle = page.locator('.header_secondary_container').locator('.title')
    this.productSort = page.locator('.right_component').locator('.product_sort_container')
    this.shoppingCart = page.locator('.shopping_cart_container').locator('.shopping_cart_link')
    this.burgerMenu = page.locator('#menu_button_container').locator('.bm-burger-button').getByRole('button')
    this.inventoryItemList = page.locator('.inventory_list')
    this.inventoryItem = page.locator('.inventory_item')
    this.shoppingCartBadge = page.locator('.shopping_cart_badge')
  }

  async goTo() {
    await this.page.goto('https://www.saucedemo.com/inventory.html')
  }

  async verifyPageLogoAndTitle() {
    await expect(this.appLogo).toHaveText('Swag Labs')
    await expect(this.pageTitle).toHaveText('Products')
  }

  async verifySortElements() {
    // Verfiy default value for product sort is Name A to Z
    await expect(this.productSort).toHaveValue('az')

    // Verify all sort options exist
    const productSortOptions = this.page.locator('.product_sort_container > option')
    await expect(productSortOptions).toHaveText(['Name (A to Z)', 'Name (Z to A)', 'Price (low to high)', 'Price (high to low)'])

    // Verify you can select all the options
    await this.productSort.selectOption('za')
    await this.productSort.selectOption('az')
    await this.productSort.selectOption('lohi')
    await this.productSort.selectOption('hilo')
  }

  async shoppingCartNavigation() {
    await this.shoppingCart.click()
    await expect(this.page).toHaveURL('https://www.saucedemo.com/cart.html')
  }

  async verifyBurgerMenuItems() {
    await this.burgerMenu.click()

    // Verify nav items
    const burgerMenuNavItem = this.page.locator('.bm-item-list > a')
    await expect(burgerMenuNavItem).toHaveText(['All Items', 'About', 'Logout', 'Reset App State'])

    // Close nav menu
    const burgerMenuCloseBtn = this.page.locator('#react-burger-cross-btn')
    await burgerMenuCloseBtn.click()
  }

  async verifyInventory() {
    await expect(this.inventoryItemList).toBeVisible()

    // Verify each inventory items has all of the correct attributes and they are visible
    for (let i = 0; i < await this.inventoryItem.count(); i++) {
      // Item image
      await expect(this.inventoryItem.nth(i).locator('.inventory_item_img > a')).toBeVisible()
      await expect(this.inventoryItem.nth(i).locator('.inventory_item_img > a > img')).toBeVisible()

      // Item description
      await expect(this.inventoryItem.nth(i).locator('.inventory_item_description')).toBeVisible()
      await expect(this.inventoryItem.nth(i).locator('.inventory_item_label')).toBeVisible()
      await expect(this.inventoryItem.nth(i).locator('.inventory_item_label > a')).toBeVisible()
      await expect(this.inventoryItem.nth(i).locator('.inventory_item_name')).toBeVisible()
      await expect(this.inventoryItem.nth(i).locator('.inventory_item_desc')).toBeVisible()

      // Item price
      await expect(this.inventoryItem.nth(i).locator('.pricebar')).toBeVisible()
      await expect(this.inventoryItem.nth(i).locator('.inventory_item_price')).toBeVisible()
      await expect(this.inventoryItem.nth(i).locator('.pricebar').getByRole('button')).toHaveText('Add to cart')
    }
  }

  async addItemToCart(itemIndex: number) {
    await this.inventoryItem.nth(itemIndex).locator('#add-to-cart-sauce-labs-backpack').click()
    await expect(this.shoppingCartBadge).toHaveText('1')
  }
}