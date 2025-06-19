import { test as setup } from '@playwright/test';
import path from 'path';

const authFile = path.join(__dirname, '../playwright/.auth/user.json');

const creds = {
  user_name: process.env.USER_NAME as string,
  password: process.env.PASSWORD as string,
}

setup('authenticate', async ({ page, baseURL }) => {
  // Perform auth steps
  await page.goto('/');
  console.log(creds);

  await page.locator('#user-name').fill(creds.user_name);
  await page.locator('#password').fill(creds.password);

  await page.locator('#login-button').click()

  await page.waitForURL(`${baseURL}/inventory.html`)

  await page.context().storageState({ path: authFile });

})