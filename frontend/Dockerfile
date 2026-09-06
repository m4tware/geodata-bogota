FROM node:22-alpine AS build
WORKDIR /frontend
COPY package.json pnpm-lock.yaml ./
RUN corepack enable && pnpm install --frozen-lockfile
COPY . .
RUN pnpm build

FROM node:22-alpine
WORKDIR /frontend
RUN corepack enable && corepack prepare pnpm@11.20.0 --activate
COPY --from=build /frontend/package.json /frontend/pnpm-lock.yaml ./
COPY --from=build /frontend/node_modules ./node_modules
COPY --from=build /frontend/dist ./dist
EXPOSE 8001
CMD ["pnpm", "preview", "--host", "0.0.0.0", "--port", "8001"]
