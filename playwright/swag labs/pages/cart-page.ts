import { type Locator, type Page } from '@playwright/test'

export class ShoppingCartPage {
  readonly page: Page
  readonly appLogo: Locator
  readonly pageTitle: Locator
  readonly shoppingCartBadge: Locator
  readonly cartListQuantityLabel: Locator
  readonly cartListDescriptionLabel: Locator
  readonly cartItemQuantity: Locator
  readonly cartItemLink: Locator
  readonly cartItemName: Locator
  readonly cartItemDescription: Locator
  readonly cartItemPrice: Locator
  readonly removeItemBtn: Locator
  readonly continueShoppingBtn: Locator
  readonly checkoutBtn: Locator

  constructor(page: Page) {
    this.page = page
    this.appLogo = page.locator('.header_label').locator('.app_logo')
    this.pageTitle = page.locator('.header_secondary_container').locator('.title')
    this.shoppingCartBadge = page.locator('.shopping_cart_badge')
    this.cartListQuantityLabel = page.locator('.cart_list').locator('.cart_quantity_label')
    this.cartListDescriptionLabel = page.locator('.cart_list').locator('.cart_desc_label')
    this.cartItemQuantity = page.locator('.cart_item').locator('.cart_quantity')
    this.cartItemLink = page.locator('.cart_item').locator('.cart_item_label').locator('.item_4_title_link')
    this.cartItemName = page.locator('.cart_item').locator('.cart_item_label').locator('.item_4_title_link').locator('.inventory_item_name')
    this.cartItemDescription = page.locator('.cart_item').locator('.cart_item_label').locator('.inventory_item_desc')
    this.cartItemPrice = page.locator('.cart_item').locator('.cart_item_label').locator('.item_pricebar').locator('.inventory_item_price')
    this.removeItemBtn = page.locator('.cart_item').locator('.cart_item_label').locator('.item_pricebar').locator('.btn')
    this.continueShoppingBtn = page.locator('#continue-shopping')
    this.checkoutBtn = page.locator('#checkout')
  }

}