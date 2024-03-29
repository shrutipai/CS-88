test = {
  'name': 'Extra Credit',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> _, code = lab08_extra_credit()
          >>> hashlib.md5(str.encode(code)).hexdigest()[:6] in ['243887', '9ba492', 'd8f102', 'a98701', 'b6dd8a', '40ee63', 'a399af', 'b7cf0d', 'b85a90', 'd20427', 'b5b8f5', '6d8351', 'd6534f', 'fb465a', 'a56932', '870c63', 'dfc3a2', 'aa1a07', 'ae96c3', '919bea', 'b3117c', 'b3919c', '17cc32', '5fb2d5', '3ff596', '305f9a', '93b9a1', '384b7e', '711d6a', 'c5008c', '02b309', '47bae6', 'bff2a1', '8b072a', '51a38e', '9880dd', '1973b3', '90460b', '3d1852', '3c6763', '99b122', '6debff', 'e2cdc6', '38de60', '682bf4', '55eee7', '9c18f8', 'f06def', 'd10d70', 'cf8c1f', '1a4dae', 'ee8c2b', '95a52c', '76cd1b', '9d1f30', 'ed9c20', 'fab44c', '9ad320', '1b1c4d', 'c1d09b', '9f8a95', '033d4d', 'cd1297', '14a241', 'e2cb12', '37fa4d', '1dcfbd', '64e9a7', '663aa5', 'beef9a', '756034', '7df52d', '6b8156', 'f46945', '36e99b', '04d541', '2e3b3b', 'a7c880', '967a2d', '887ca5', 'ee039d', '68961f', '0dda69', 'b17bba', '82b8cf', '508a43', 'b022a4', 'a4f9a3', 'ee7a03', '3c7eea', 'e6095d', '9dc8c9', '6043df', 'cea6fd', '30d652', '3bb49b', 'f63c2a', 'a5f421', '62d016', '1ce0db', 'c421d2', '1f2d8a', '068820', 'a4b739', 'e7c440', '6eab93', 'de32e0', 'c33bfc', 'c1c51a', '2b20fd', 'ec6c10', '532abf', '99bb38', '0f90a2', 'b896eb', '53d357', '40a69e', '02f7d8', 'ddb726', '0c700e', '0a5cd0', '03a293', '6f0e1e', '01709a', 'cf230e', '79d6e0', '070974', '53fd1a', '552024', '077ab5', '8ed8fc', 'be4567', '7d3cf3', '2ff459', '919116', '79f4de', '15dc98', '0313c4', 'd4d767', '009a6f', '4837dd', '621deb', '7ca7a3', 'fa0fb5', 'cb7068', 'f8a45b', '51cfb7', 'ad6a4e', 'c68c91', '9a2672', '129a31', '1c1e6a', '366e01', 'e409e1', 'f20a12', '449dc8', '8ce4f2', '511509', '4e6d8b', '63d960', '1ea506', '8de309', 'cb3caa', 'eb396a', '3b2062', 'c8268b', '50cfcf', '3d7cf2', '78a08a', '0b2c64', 'c96d0d', 'a6e76e', '69fcef', '75d8fa', '1f99d5', 'f23a20', '7edd1f', 'c5681c', 'd30a36', '61bcc2', 'a02321', '1f2a81', 'ae06e1', '97bd06', '3af636', '020bbd', '2a7f5d', 'c8e31c', '1266d8', '606269', '5b97cf', 'c268ef', '58b756', '82877f', '8a4ba1', 'e0cd22', '290dab', 'ef58c6', '0ab186', '988035', 'b9e5b9', 'beab72', '3ff9fd', 'e01297', '0fa80a', '9e3b83', '6a5535', 'c22c11', 'd10f94', '978181', '37eff2', '9a4266', '8bd052', '3d5cd9', '201589', '116575', '5b06a3', '418c82', 'e80269', '7e8d44', 'be17c5', 'f78786', '30821a', '8f5056', '12be72', 'ffea4b', 'b27919', 'df8039', '79fde2', '8e97b7', 'c8c4fa', 'dfa93e', 'f955e2', '684915', 'f9018d', '25a592', '74c453', '88937b', '4f0146', '13df95', 'a14c8e', '4371eb', '482042', 'c36a97', 'b226b3', '0fc07f', 'c17474', '7c9b00', '34d92b', 'b27673', 'a8cf05', '468bb7', '6680f2', 'c1e86c', 'efd2b4', '7b6508', 'ea8340', 'bc3fda', '92c524', 'c2f213', 'e977bb', 'aec2fa', '22b0b8', '01234e', 'a5af4b', '84339d', '38b065', '89fcdf', '95ba39', '5268bc', '8bd97f', 'ea9f3f', '1bfa0e', '477e6f', 'b836fa', 'f00ec2', '16d43f', '198521', 'e3a70f', '97ecd3', '1ca839', '993971', 'c549a1', '024b5a', 'e212f9', '2471fc', 'ef76ec', 'ac1f83', '7b8013', 'f030bb', '3ed379', 'a2acc1', '4de565', '39be39', '6e8453', '58fbc7', '839b7e', 'bb6573', 'dd6fb0', '087d6a', 'e7dc18', '3f0caf']
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from lab08 import *
      >>> import hashlib
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
