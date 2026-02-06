import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Matcha Market",
  description: "Ecommerce store for everything matcha",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>
        {children}
      </body>
    </html>
  );
}
