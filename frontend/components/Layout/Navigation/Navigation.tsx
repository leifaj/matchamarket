import Link from 'next/dist/client/link';
import styles from '../Navigation/Navigation.module.css';

export default function Navigation() {
    return(
        <nav className={styles.nav}>
            <ul className={styles.navList}>
                <li className={styles.navItem}><Link href="/shop">shop</Link></li>
                <li className={styles.navItem}><Link href="/about">about</Link></li>
                <li className={styles.navItem}><Link href="/faq">faq</Link></li>
            </ul>
        </nav>
    )
}