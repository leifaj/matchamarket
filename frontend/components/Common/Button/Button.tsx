import styles from '@components/Common/Button.module.css';

export default function Button({ buttonText }: { buttonText: string }) {
    return(
        <button className={styles.button}>{buttonText}</button>
    )   
}