import { type Locator, type Page } from '@playwright/test';

export class InventoryPage {
  readonly page: Page
  readonly appLogo: Locator
  readonly pageTitle: Locator
  readonly inventoryItemList: Locator
  readonly productSort: Locator
  readonly shoppingCart: Locator
  readonly burgerMenu: Locator
}