export default function Navigation() {
    return(
        <nav className="w-full">
            <ul className="w-full flex flex-row flex-nowrap justify-end list-none space-x-8">
                <li className="text-light-blue hover:text-medium-blue"><a className="w-full">Home</a></li>
                <li className="text-light-blue hover:text-medium-blue"><a className="w-full">Shop</a></li>
                <li className="text-light-blue hover:text-medium-blue"><a className="w-full">About</a></li>
                <li className="text-light-blue hover:text-medium-blue"><a className="w-full">Contact</a></li>
            </ul>
        </nav>
    )
}