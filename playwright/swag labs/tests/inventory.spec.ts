import { test } from '@playwright/test'
import { InventoryPage } from '../pages/inventory-page'

test.describe('Inventory Page', () => {
  let inventoryPage: any

  test.beforeEach(async ({ page }) => {
    inventoryPage = new InventoryPage(page)
  })

  test.describe('Inventory Page', () => {
    test('Verify page elements', async () => {
      await inventoryPage.goTo()
      await inventoryPage.verifyPageLogoAndTitle()
      await inventoryPage.verifyBurgerMenuItems()
      await inventoryPage.verifySortElements()
      await inventoryPage.verifyInventory()
    })
  })

  test.describe('Shopping Cart Interactions', () => {
    // Can change based on what item you want to target
    const itemIndex = 0
    test('Add/Remove item to/from cart', async () => {
      await inventoryPage.goTo()
      await inventoryPage.addItemToCart(itemIndex)
      await inventoryPage.removeItemFromCart(itemIndex)
    })
  })
})