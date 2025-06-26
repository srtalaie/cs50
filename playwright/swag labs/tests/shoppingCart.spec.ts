import { test, } from '@playwright/test'
import { InventoryPage } from '../pages/inventory-page'

test.describe('Shopping Cart Page', () => {
  let inventoryPage: any
  const itemIndex = 0

  test.beforeEach(async ({ page }) => {
    inventoryPage = new InventoryPage(page)
  })

  test.only('Add item to cart', async () => {
    await inventoryPage.goTo()
    await inventoryPage.addItemToCart(itemIndex)
  })
})