# **Installation**

[[toc]]

## **Getting Ready**

- clone the repo

```bash
git clone https://github.com/Himasnhu-at/uci_integration.git
```

- things to be installed:

```bash
python3
python3-venv
npm # for docs
```

## **Dev Setup**

- install requirements

```bash
npm i
```

- setup dev-docs

```bash
npm install
```

## **Running the Project**

- migrate dB

```bash
npm run prisma:dev:deploy
```

- run the app

```bash
npm run start:dev
```

- run the docs

```bash
npm run docs:dev
```

## **Project Structure**

- dev-docs/: This directory contains the documentation for your project.

- src/: This directory contains all the code related to your application.

- prisma/: This directory contains the Prisma schema and migration files.
