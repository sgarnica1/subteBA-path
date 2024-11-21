import { StationsType } from '../types/types';
import Sidebar from './Sidebar';

type LayoutProps = {
  stations: StationsType[]
  children: React.ReactNode;
};

const Layout = ({ stations, children }: LayoutProps) => {

  const options = stations.map(station => ({
    value: station.id,
    label: station.name,
  }))

  return (
    <div className="relative w-screen h-screen flex flex-col-reverse md:flex-row">
      <Sidebar options={options} />
      <div className='flex-1 relative'>
        {children}
      </div>
    </div>
  );
};

export default Layout;