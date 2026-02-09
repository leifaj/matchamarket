import Link from 'next/link';
import Button from '../components/Common/Button/Button';
import styles from './page.module.css';

export default function Home() {
  return (
    <div className={styles.container}>
      <div className={styles.hero}>
        <div className={styles.heroHeader}>
          <span className={styles.heroText}>for the love of matcha</span>
          <Link href="/shop">
            <Button buttonText="Shop Now"/>
          </Link>
        </div>
        <img src="/matcha-whisked.jpeg" alt="whisked matcha" className={styles.heroImage} />
      </div>
    </div>
  );
}
