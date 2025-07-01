import { test } from '@playwright/test'
import { InventoryPage } from '../pages/inventory-page'
import { NavBar } from '../pages/navbar-page'

test.describe('Inventory Page', () => {
  let inventoryPage: any
  let navBarPage: any

  test.beforeEach(async ({ page }) => {
    inventoryPage = new InventoryPage(page)
    navBarPage = new NavBar(page)
  })

  test.describe('Inventory Page', () => {
    test('Verify page elements', async () => {
      await inventoryPage.goTo()
      await inventoryPage.verifyTitle()
      await navBarPage.verifyAppLogo()
      await navBarPage.verifyBurgerMenuItems()
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