import type { Metadata } from "next";
import "./globals.css";
import Header from "../components/Layout/Header/Header";
import Footer from "../components/Layout/Footer/Footer";
import Main from "../components/Layout/Main/Main";

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
        <Header />
        <Main>{children}</Main>
        <Footer />
      </body>
    </html>
  );
}
