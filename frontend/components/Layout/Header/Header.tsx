
import React from 'react'; 
import Logo from '../../Common/Logo/Logo';
import Navigation from '../Navigation/Navigation';
import ShopIcons from '../ShopIcons/ShopIcons';
import styles from './Header.module.css';

export default function Header() {
    return(
        <header className={styles.header}>
            <Logo />
            <Navigation />
            <ShopIcons />
        </header>
    )
}