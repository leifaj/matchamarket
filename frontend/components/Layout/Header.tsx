
import React from 'react'; 
import Logo from '../Common/Logo';
import Navigation from '../Layout/Navigation';

export default function Header() {
    return(
        <header className='w-full flex items-center justify-between px-6 py-4 border-b border-gray-300'>
            <Logo />
            <Navigation />
        </header>
    )
}