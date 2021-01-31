import React, { FC , useState } from 'react';
import { Map } from 'react-kakao-maps';
  
declare global {
  interface Window {
    kakao: any;
  }
}

const { kakao } = window;

const KakaoMap: FC = () => {
  const [option, setOption] = useState({
    center : new kakao.maps.LatLng(37.34490572458397, 126.73239490408842),
    level: 3
  });

  return (
    <>
      <div className="map_wrap" style={{ width: '100%', height:'80vh' }}>
        <Map options={option}>
        </Map>
      </div>
    </>
  )
}

export default KakaoMap;
