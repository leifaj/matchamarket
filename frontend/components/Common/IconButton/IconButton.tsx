import styles from '../IconButton/IconButton.module.css';
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';

export default function IconButton({faIcon}: {faIcon: any}) {
    return(
        <button className={styles.button}>
            <FontAwesomeIcon icon={faIcon} className={styles.icon} />
        </button>
    )   
}