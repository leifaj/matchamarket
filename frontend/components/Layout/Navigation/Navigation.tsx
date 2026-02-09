import styles from '../Navigation/Navigation.module.css';

export default function Navigation() {
    return(
        <nav className={styles.nav}>
            <ul className={styles.navList}>
                <li className={styles.navItem}><a className={styles.navLink}>shop</a></li>
                <li className={styles.navItem}><a className={styles.navLink}>about</a></li>
                <li className={styles.navItem}><a className={styles.navLink}>faq</a></li>
            </ul>
        </nav>
    )
}