type LayoutProps = {
  children: React.ReactNode;
};

const Layout = ({ children }: LayoutProps) => {
  return (
    <div className="relative w-screen h-screen">
      {children}
    </div>
  );
};

export default Layout;