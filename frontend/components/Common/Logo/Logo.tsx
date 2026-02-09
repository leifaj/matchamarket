import Link from 'next/dist/client/link';
import styles from './Logo.module.css';

export default function Logo() {
    return(
        <Link href="/">
            <img src="/matchamarket_logo_nowrap.png" alt="Matcha Market Logo" className={styles.logo} />
        </Link>
    )   
}