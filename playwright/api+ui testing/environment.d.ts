declare global {
  namespace NodeJS {
    interface ProcessEnv {
      FIRST_NAME: string
      LAST_NAME: string
      EMAIL: string
      PASSWORD: string
    }
  }
}

export { };

