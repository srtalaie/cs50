import { test as setup } from '@playwright/test';
import path from 'path';

const authFile = path.join(__dirname, '../playwright/.auth/user.json');

const creds = {
  user_name: process.env.USER_NAME as string,
  password: process.env.PASSWORD as string,
}

setup('authenticate', async ({ page, baseURL }) => {
  await page.goto('/');

  await page.getByPlaceholder('Username').fill(creds.user_name);
  await page.getByPlaceholder('Password').fill(creds.password);

  await page.locator('input[type="submit"]').click()

  await page.waitForURL(`${baseURL}/inventory.html`)

  await page.context().storageState({ path: authFile });

})