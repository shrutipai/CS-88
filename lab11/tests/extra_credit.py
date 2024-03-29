test = {
  'name': 'Extra Credit',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> _, code = lab11_extra_credit()
          >>> hashlib.md5(str.encode(code)).hexdigest()[:6] in ['13b6ad', '62fb21', 'f4e62a', '1ef391', '48298e', '7799f3', '5e8480', '060b32', '4e9388', '89bbc3', '910a08', '56e3ce', '9d7270', '2c3ee3', 'a9dc65', '354d3f', 'fba9c5', '1be646', 'bfbb3d', 'ee0857', 'e75826', '3bcde1', 'e18b64', '3a879f', '7edfa9', '552a0f', '2db3d3', '986990', 'a4f1c2', '7b0941', '14e228', '29e8b8', '3b3817', '6aedfe', '693335', 'dc74a7', 'a1cd29', 'd6c02f', '931868', 'd1d7f6', '54208e', '5c5805', '1fb8f3', '12c223', 'd28cae', '90394b', 'dcc29c', 'c354b7', '90627e', 'c29989', '47fa4f', '12cc92', '9b3985', '96ee43', 'a13305', '817968', 'f71f05', '252d00', 'cd6071', 'bae67d', '3c5b48', '41ce09', '27a083', '69ff24', '5b1b2c', '010d7b', 'ad33a0', '09f53c', '354315', '99eeb2', 'f965b2', '0f8a08', '4d6515', '5d33c8', '96dc29', 'e9d6ee', '32e994', '392240', 'd8ce67', '9391b6', 'fdff6a', '3a10ce', '835213', '8d4541', '7d8b3f', '05bda9', 'b815df', '2df564', '8f7a5a', '53c2b3', 'dda6c9', 'cd1117', 'd7caec', '93d14a', 'fc951a', 'dcdc60', '4121a4', '3f615f', '32fb03', '1fbd3c', '33bb03', 'dcc621', 'fe5d97', 'b2f76c', 'c100dc', '150006', '07ec66', '1e2a79', '1196e8', '0e80e6', '9e9538', '6c1f9c', 'a81866', 'e75fc9', '09787c', 'a1400f', '6598b2', '50895b', '681c60', 'ede0a4', 'b73188', '13a427', '2a631b', '8def95', '12b185', '7fdb3e', '1df606', '2dbadd', 'b57589', '58168c', 'ed2ae3', 'f33b60', '3165a0', '69be1a', 'bae25a', 'bd48fc', '55d923', '671fb9', '5571b7', '2629e9', '5df4c7', '30c094', '40d3f4', '35a84d', '613a9e', 'db8872', 'f4007c', 'c9ea4e', 'ceea6e', 'efacff', 'f85eac', 'ca8303', '34b129', '2d8997', '19eb83', '54860a', '9d0c44', 'b17eb8', '70e15e', 'a2d766', 'fc77a0', '335957', 'c85443', '50af82', '79efa9', 'b69c70', '4b824e', '42d140', '61109c', '034633', '88cabf', '996d20', '13ce72', '451ae4', '775952', '9ba26c', '105bc1', 'ddd8d1', '5ccb81', '5ab25c', '2641ad', '735c02', 'a75f1a', 'b0b302', 'a1705e', '833868', '67cd98', '533698', 'cb7ba9', '784abd', '14b92f', '096df3', '909e12', '3e74e9', '3328d3', '7c4c1f', '5459f1', '94200d', '8a68ef', '94db4a', 'a58e01', '791b64', 'f72851', '6cf5f5', '1eac61', 'b17ced', '889eb0', '9cca95', '8bb4db', 'def340', '2165d6', '63329f', '9da8ef', '4fe525', '537e10', '9cf616', '7eae7b', '3c4df9', 'dab041', '9f6c18', 'aa0c34', 'c0c640', '697ba5', 'e7efe7', '518587', 'fa9a7c', '9ab7a6', '1230d4', '288ca8', 'ce8cb3', 'c26b8e', 'a0a514', '488aef', 'ff4832', 'be789a', 'fc090b', '2eae37', '7c9c2d', '982ed7', '5d7ef4', 'c45a17', '20c9fa', '28e91c', '6af846', 'ba4f66', 'f57a7a', '2677e8', '6d0143', '5b9f93', 'b65695', '4af4ff', '76069c', 'aa7f50', '910167', '05b3d1', 'd3396f', '1a5107', '58550c', '6b6ba3', 'ed0042', 'b3ec47', '14ffa5', 'ded9b6', '7447c9', '56a309', 'e3b66f', 'b72252', 'd3d463', '843e03', '24a2b2', '5c4ff8', '72bbf6', 'da7b77', '646cb6', '4dede9', 'f6af37', '4c644d', '29fc41', '2483e3', '560823', '8f9c85', '19f4df', 'cdd4da', 'a90864', 'f43ca6', '1a9abb', 'ad420b', '6d12aa', '3d2e25', 'aae1f9', '60bcdf', '2c257a', 'eeea13', 'bd721e', '5c380b', 'aa99b6', '25171d', 'a9bdcc', '576e8d', '1617cb', '23cd20', 'e0efb4']
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from lab11 import *
      >>> import hashlib
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
