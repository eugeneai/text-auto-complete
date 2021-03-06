from nose.tools import raises, nottest
from isu.autocomplete import analysis, preproc
import pprint


class TestLoader:
    def setUp(self):
        pass

    def tearDown(self):
        pass

    #@nottest
    def test_1_tokenizer(self):
        preproc.main()

    #@nottest
    def test_2_tokenizer_mkb10(self):
        TXT = "пациент доволен"
        mkb10 = "I80.36"
        d = {}
        d = preproc.tokenizer(TXT, d, mkb10=mkb10)
        # raise RuntimeError(d)
        print(d)
        data = d[('пациент', 'довольный')]
        print("frequences", data)
        assert isinstance(data, dict)
        c = data[""]
        assert isinstance(c, int)
        assert c == 1
        print("Orig d:", d)
        helm = analysis.Helm(d)
        print("TrieStruct", [t.trie_idx for t in helm.tries])
        print("Test:", helm.query("I8", prefixes=["пац",  "дов"]))
        # Hans Zimmer

    def test_4_preparation(self):
        from isu.autocomplete import load
        phrases = load.main()
        assert phrases

    #@nottest
    def test_30_run_main(self):
        helm = analysis.main()
        prf = ["гип", "арт"]
        rc = helm.query(mkb10="C1", prefixes=prf)
        print("Prefixes:", prf)
        print("List: C1")
        pprint.pprint(rc)
        rc = helm.query(mkb10="C", prefixes=["гип", "арт"])
        print("List: C")
        pprint.pprint(rc)
        rc = helm.query(mkb10="", prefixes=["гип", "арт"])
        print("List: ''")
        pprint.pprint(rc)

        assert isinstance(rc, set)
        # assert len(rc[0]) == 2
