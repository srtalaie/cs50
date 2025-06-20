import { test } from '@playwright/test'
import { InventoryPage } from '../pages/inventory-page'

test.only('Inventory Page', async ({ page }) => {
  const inventoryPage = new InventoryPage(page)

  await inventoryPage.goTo()
  await inventoryPage.verifyPageLogoAndTitle()
  await inventoryPage.verifyBurgerMenuItems()
  await inventoryPage.verifySortElements()
  await inventoryPage.verifyInventory()
})