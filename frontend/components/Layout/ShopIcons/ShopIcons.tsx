import styles from '../ShopIcons/ShopIcons.module.css';
import IconButton from '../../Common/IconButton/IconButton';

import { faSearch, faCartShopping } from '@fortawesome/free-solid-svg-icons';

export default function ShopIcons() {
    return(
        <ul className={styles.iconList}>
            <li className={styles.iconListItem}>
                <IconButton faIcon={faSearch} />
            </li>
            <li className={styles.iconListItem}>
                <IconButton faIcon={faCartShopping} />
            </li>
        </ul>
    )
}