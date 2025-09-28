import type { NextConfig } from 'next';
const path = require('path');

const nextConfig: NextConfig = {
  compiler: {
    removeConsole: process.env.NODE_ENV === 'production',
  },
  reactStrictMode: false,
  eslint: {
    ignoreDuringBuilds: true,
  },
  images: {
    unoptimized: true,
  },
  trailingSlash: false,
  // Removing static export to fix clientModules error
  // output: 'export',
};

export default nextConfig;
