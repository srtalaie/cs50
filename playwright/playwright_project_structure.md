# Playwright Project Structure & Utils Examples

## Complete Project File Structure

```
my-playwright-project/
├── playwright.config.js                 # Main configuration file
├── package.json
├── .env                                 # Environment variables
├── .gitignore
├── README.md
│
├── tests/                               # All test files
│   ├── auth/
│   │   ├── login.spec.js
│   │   ├── registration.spec.js
│   │   └── password-reset.spec.js
│   ├── e2e/
│   │   ├── checkout-flow.spec.js
│   │   ├── user-journey.spec.js
│   │   └── search-functionality.spec.js
│   ├── api/
│   │   ├── user-api.spec.js
│   │   ├── products-api.spec.js
│   │   └── orders-api.spec.js
│   └── visual/
│       ├── homepage-visual.spec.js
│       └── product-page-visual.spec.js
│
├── pages/                               # Page Object Model classes
│   ├── base-page.js                     # Common page functionality
│   ├── login-page.js
│   ├── product-page.js
│   ├── checkout-page.js
│   ├── dashboard-page.js
│   └── components/                      # Reusable UI components
│       ├── header-component.js
│       ├── navigation-component.js
│       ├── modal-component.js
│       └── product-card-component.js
│
├── utils/                               # Utility functions (detailed below)
│   ├── test-helpers.js                  # Test-specific utilities
│   ├── data-generators.js               # Test data creation
│   ├── api-helpers.js                   # API interaction utilities
│   ├── database-helpers.js              # Database operations
│   ├── file-helpers.js                  # File operations
│   ├── email-helpers.js                 # Email testing utilities
│   ├── date-helpers.js                  # Date/time utilities
│   ├── validation-helpers.js            # Data validation
│   ├── browser-helpers.js               # Browser-specific utilities
│   └── custom-matchers.js               # Custom Playwright matchers
│
├── fixtures/                            # Test fixtures and setup
│   ├── auth.setup.js                    # Authentication setup
│   ├── database.setup.js                # Database seeding
│   └── global.setup.js                  # Global test setup
│
├── data/                                # Test data files
│   ├── users.json                       # User test data
│   ├── products.json                    # Product test data
│   ├── test-files/                      # Files for upload testing
│   │   ├── sample.pdf
│   │   ├── test-image.jpg
│   │   └── large-file.zip
│   └── mock-responses/                  # API mock data
│       ├── user-response.json
│       └── products-response.json
│
├── config/                              # Configuration files
│   ├── environments/
│   │   ├── dev.config.js
│   │   ├── staging.config.js
│   │   └── prod.config.js
│   └── test.config.js
│
├── reports/                             # Test reports and artifacts
│   ├── html-report/
│   ├── test-results/
│   └── screenshots/
│
└── .github/                             # CI/CD workflows
    └── workflows/
        ├── playwright.yml
        └── visual-regression.yml
```

## Utils Folder Deep Dive

The `utils/` folder contains helper functions that don't belong in Page Objects or tests. Here are detailed examples:

### 1. test-helpers.js
```javascript
// Generic test utilities that work across multiple test scenarios
export class TestHelpers {
  // Wait for multiple elements to be ready
  static async waitForElementsToLoad(page, selectors) {
    const promises = selectors.map(selector => 
      page.locator(selector).waitFor({ state: 'visible' })
    );
    await Promise.all(promises);
  }

  // Take screenshot with timestamp
  static async takeTimestampedScreenshot(page, name) {
    const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
    await page.screenshot({ 
      path: `screenshots/${name}-${timestamp}.png`,
      fullPage: true 
    });
  }

  // Retry function with exponential backoff
  static async retryWithBackoff(fn, maxRetries = 3) {
    for (let i = 0; i < maxRetries; i++) {
      try {
        return await fn();
      } catch (error) {
        if (i === maxRetries - 1) throw error;
        await this.sleep(Math.pow(2, i) * 1000);
      }
    }
  }

  // Smart sleep that waits for network idle
  static async waitForNetworkIdle(page, timeout = 5000) {
    await page.waitForLoadState('networkidle', { timeout });
  }

  static sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
}
```

### 2. data-generators.js
```javascript
// Generate realistic test data dynamically
import { faker } from '@faker-js/faker';

export class DataGenerator {
  // Generate user data with realistic constraints
  static generateUser(overrides = {}) {
    return {
      firstName: faker.person.firstName(),
      lastName: faker.person.lastName(),
      email: faker.internet.email(),
      password: 'TestPass123!',
      dateOfBirth: faker.date.birthdate({ min: 18, max: 80, mode: 'age' }),
      address: {
        street: faker.location.streetAddress(),
        city: faker.location.city(),
        zipCode: faker.location.zipCode(),
        country: 'US'
      },
      ...overrides
    };
  }

  // Generate product data
  static generateProduct() {
    return {
      name: faker.commerce.productName(),
      price: faker.commerce.price({ min: 10, max: 1000 }),
      description: faker.commerce.productDescription(),
      category: faker.commerce.department(),
      sku: faker.string.alphanumeric(10).toUpperCase(),
      inStock: faker.datatype.boolean()
    };
  }

  // Generate credit card data for testing
  static generateCreditCard() {
    return {
      number: '4111111111111111', // Test card number
      expiryMonth: '12',
      expiryYear: '2025',
      cvv: '123',
      holderName: faker.person.fullName()
    };
  }

  // Generate unique identifiers
  static generateUniqueId(prefix = 'test') {
    return `${prefix}_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
  }
}
```

### 3. api-helpers.js
```javascript
// API interaction utilities that aren't page-specific
export class ApiHelpers {
  constructor(baseURL, apiKey = null) {
    this.baseURL = baseURL;
    this.apiKey = apiKey;
  }

  // Generic API request with error handling
  async makeRequest(endpoint, options = {}) {
    const url = `${this.baseURL}${endpoint}`;
    const defaultOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(this.apiKey && { 'Authorization': `Bearer ${this.apiKey}` })
      }
    };

    const response = await fetch(url, { ...defaultOptions, ...options });
    
    if (!response.ok) {
      throw new Error(`API request failed: ${response.status} ${response.statusText}`);
    }

    return await response.json();
  }

  // Create test user via API (faster than UI)
  async createTestUser(userData) {
    return await this.makeRequest('/api/users', {
      method: 'POST',
      body: JSON.stringify(userData)
    });
  }

  // Clean up test data
  async deleteTestUser(userId) {
    return await this.makeRequest(`/api/users/${userId}`, {
      method: 'DELETE' 
    });
  }

  // Set up test data state
  async setupTestData(scenario) {
    switch (scenario) {
      case 'empty-cart':
        return await this.makeRequest('/api/test/reset-cart', { method: 'POST' });
      case 'full-inventory':
        return await this.makeRequest('/api/test/stock-all-products', { method: 'POST' });
      default:
        throw new Error(`Unknown test scenario: ${scenario}`);
    }
  }
}
```

### 4. database-helpers.js
```javascript
// Database operations for test setup/cleanup
export class DatabaseHelpers {
  constructor(connectionString) {
    this.connection = connectionString;
  }

  // Seed database with test data
  async seedTestData() {
    // Implementation depends on your database
    // Could use Prisma, TypeORM, or raw SQL
    console.log('Seeding test database...');
  }

  // Clean up test data after tests
  async cleanupTestData() {
    // Remove test users, orders, etc.
    console.log('Cleaning up test data...');
  }

  // Create isolated test database
  async createTestDatabase(testName) {
    const dbName = `test_${testName}_${Date.now()}`;
    // Create and return database connection
    return dbName;
  }

  // Reset database to known state
  async resetToCleanState() {
    // Truncate tables, reset sequences, etc.
    console.log('Resetting database to clean state...');
  }
}
```

### 5. email-helpers.js
```javascript
// Email testing utilities
export class EmailHelpers {
  constructor(emailService) {
    this.emailService = emailService; // Could be MailHog, Mailtrap, etc.
  }

  // Wait for email to arrive
  async waitForEmail(recipient, subject, timeout = 30000) {
    const startTime = Date.now();
    
    while (Date.now() - startTime < timeout) {
      const emails = await this.getEmails(recipient);
      const email = emails.find(e => e.subject.includes(subject));
      
      if (email) {
        return email;
      }
      
      await new Promise(resolve => setTimeout(resolve, 1000));
    }
    
    throw new Error(`Email with subject '${subject}' not received within ${timeout}ms`);
  }

  // Extract verification link from email
  extractVerificationLink(emailContent) {
    const linkRegex = /https?:\/\/[^\s]+verify[^\s]*/i;
    const match = emailContent.match(linkRegex);
    return match ? match[0] : null;
  }

  // Clear all emails (for test isolation)
  async clearAllEmails() {
    // Implementation depends on email service
    console.log('Clearing all test emails...');
  }
}
```

### 6. file-helpers.js
```javascript
// File operations and validations
import fs from 'fs';
import path from 'path';

export class FileHelpers {
  // Create temporary file for testing uploads
  static createTempFile(fileName, content = 'test content') {
    const filePath = path.join(__dirname, '../temp', fileName);
    fs.writeFileSync(filePath, content);
    return filePath;
  }

  // Validate downloaded file
  static async validateDownload(downloadPath, expectedSize = null) {
    if (!fs.existsSync(downloadPath)) {
      throw new Error(`Downloaded file not found: ${downloadPath}`);
    }

    const stats = fs.statSync(downloadPath);
    
    if (expectedSize && stats.size !== expectedSize) {
      throw new Error(`File size mismatch. Expected: ${expectedSize}, Got: ${stats.size}`);
    }

    return {
      exists: true,
      size: stats.size,
      lastModified: stats.mtime
    };
  }

  // Clean up temporary files
  static cleanupTempFiles() {
    const tempDir = path.join(__dirname, '../temp');
    if (fs.existsSync(tempDir)) {
      fs.rmSync(tempDir, { recursive: true, force: true });
    }
  }

  // Compare files (useful for download verification)
  static filesAreEqual(file1Path, file2Path) {
    const file1 = fs.readFileSync(file1Path);
    const file2 = fs.readFileSync(file2Path);
    return file1.equals(file2);
  }
}
```

### 7. custom-matchers.js
```javascript
// Custom Playwright matchers for domain-specific assertions
import { expect } from '@playwright/test';

expect.extend({
  // Custom matcher for shopping cart
  async toHaveItemsInCart(page, expectedCount) {
    const cartCount = await page.locator('[data-testid="cart-count"]').textContent();
    const actualCount = parseInt(cartCount) || 0;
    
    return {
      message: () => `Expected cart to have ${expectedCount} items, but got ${actualCount}`,
      pass: actualCount === expectedCount,
    };
  },

  // Custom matcher for form validation
  async toHaveValidationError(locator, expectedMessage) {
    const errorElement = locator.locator('[data-testid="error-message"]');
    const isVisible = await errorElement.isVisible();
    
    if (!isVisible) {
      return {
        message: () => 'Expected validation error to be visible',
        pass: false,
      };
    }

    const actualMessage = await errorElement.textContent();
    return {
      message: () => `Expected error message "${expectedMessage}", got "${actualMessage}"`,
      pass: actualMessage === expectedMessage,
    };
  }
});
```

## Key Differences: Utils vs Page Objects vs Tests

### Utils Contains:
- **Cross-cutting concerns** that multiple pages/tests need
- **Business logic helpers** that don't belong to specific pages
- **Infrastructure utilities** (database, API, file operations)
- **Test setup/teardown** functions
- **Data generation** and manipulation
- **Third-party service integrations** (email, payment processors)

### Page Objects Contain:
- **Page-specific locators** and interactions
- **UI workflow methods** for that specific page
- **Page navigation** and state management
- **Element-specific assertions** and validations

### Tests Contain:
- **Test scenarios** and user journeys
- **Assertions** and expectations
- **Test data setup** for specific scenarios
- **Orchestration** of page objects and utilities

This structure keeps your code organized, maintainable, and follows the single responsibility principle. Utils handle the "how to do common things," Page Objects handle "how to interact with specific pages," and Tests handle "what scenarios to verify."