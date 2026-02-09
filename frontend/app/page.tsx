import styles from './page.module.css';


export default function Home() {
  return (
    <div className={styles.container}>
      <div className={styles.hero}>
        <span className={styles.heroText}>for the love of matcha</span>
        <img src="/matcha-whisked.jpeg" alt="whisked matcha" className={styles.heroImage} />
      </div>

      <div className={styles.section}>
        <h1>Welcome to Matcha Market!</h1>
        <p>Your one-stop shop for all things matcha. Explore our wide selection of premium matcha products, from ceremonial grade to culinary grade, and discover the perfect matcha for your needs. Whether you're a matcha connoisseur or just starting your matcha journey, we have something for everyone. Enjoy the rich flavors and health benefits of matcha with us!</p>
      </div>
    </div>
  );
}
