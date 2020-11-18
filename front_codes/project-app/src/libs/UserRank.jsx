import React from 'react'
import { Table } from 'antd';

const columns = [
    {
      title: 'Rank',
      dataIndex: 'rank',
      sorter: {
        compare: (a, b) => b.rank - a.rank,
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
        compare: (a, b) => a.ts - b.ts,
        multiple: 4,
      },
    },
    {
      title: '급가속 횟수',
      dataIndex: 'ra',
      sorter: {
        compare: (a, b) => a.ra - b.ra,
        multiple: 3,
      },
    },
    {
      title: '급제동 횟수',
      dataIndex: 'sb',
      sorter: {
        compare: (a, b) => a.sb - b.sb,
        multiple: 2,
      },
    },
    {
      title: '급핸들링 횟수',
      dataIndex: 'sh',
      sorter: {
        compare: (a, b) => a.sh - b.sh,
        multiple: 1,
      },
    },
  ];

const data = [
  {
    key: '1',
    rank: 1,
    name: '김세환',
    ts: 58,
    ra: 24,
    sb: 31,
    sh: 38,
  },
  {
    key: '2',
    rank: 2,
    name: '이용범',
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
