import { test, expect } from '@playwright/test';

test('Login exitoso en SauceDemo', async ({ page }) => {
  // 1. Visitar la página de pruebas
  await page.goto('https://www.saucedemo.com/');

  // 2. Ingresar el usuario
  await page.locator('[data-test="username"]').fill('standard_user');

  // 3. Ingresar la contraseña
  await page.locator('[data-test="password"]').fill('secret_sauce');

  // 4. Hacer clic en el botón de Login
  await page.locator('[data-test="login-button"]').click();

  // 5. Validación: Confirmar que la URL cambió al inventario
  await expect(page).toHaveURL(/.*inventory.html/);
});