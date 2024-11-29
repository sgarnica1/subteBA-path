type TooltipProps = {
  name: string;
}

const Tooltip = ({ name }: TooltipProps) => {
  return (
    <div
      style={{
        position: 'absolute',
        top: '-30px',
        left: '50%',
        transform: 'translateX(-50%)',
        backgroundColor: '#FFFFFF',
        color: '#000000',
        padding: '4px 8px',
        borderRadius: '4px',
        fontSize: '12px',
        fontWeight: 'bold',
        whiteSpace: 'nowrap',
        boxShadow: '0 2px 4px rgba(0, 0, 0, 0.2)',
        pointerEvents: 'none',
        zIndex: 10,
      }}
    >
      {name}
    </div>
  )
}

export default Tooltip