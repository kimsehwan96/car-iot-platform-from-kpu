import React from 'react'
import { Table } from 'antd';

const columns = [
    {
      title: 'Rank',
      dataIndex: 'rank',
      sorter: {
        compare: (a, b) => a.chinese - b.chinese,
        multiple: 5,
      },
    },
    {
      title: 'UserName',
      dataIndex: 'name',
    },
    {
      title: '총합 스코어',
      dataIndex: 'ts',
      sorter: {
        compare: (a, b) => a.chinese - b.chinese,
        multiple: 4,
      },
    },
    {
      title: '급가속 횟수',
      dataIndex: 'ra',
      sorter: {
        compare: (a, b) => a.math - b.math,
        multiple: 3,
      },
    },
    {
      title: '급제동 횟수',
      dataIndex: 'sb',
      sorter: {
        compare: (a, b) => a.english - b.english,
        multiple: 2,
      },
    },
    {
      title: '급핸들링 횟수',
      dataIndex: 'sh',
      sorter: {
        compare: (a, b) => a.english - b.english,
        multiple: 1,
      },
    },
  ];

const data = [
  {
    key: '1',
    rank: '1',
    name: 'kimsehwan',
    ts: 58,
    ra: 24,
    sb: 31,
    sh: 38,
  },
  {
    key: '2',
    rank: '2',
    name: 'leeyongbeom',
    ts: 49,
    ra: 30,
    sb: 40,
    sh: 30,
  },
];


export default function UserRank() {
  function onChange(pagination, filters, sorter, extra) {
    console.log('params', pagination, filters, sorter, extra);
  }
    return (
        <div className="userrank">
            <Table
              columns={columns}
              dataSource={data}
              onChange={onChange}
            />
        </div>
    )
}
