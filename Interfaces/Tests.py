
from unittest import TestCase

from Objects.Board import Board
from Objects.Plane import Plane, PlaneError


class TestBoard(TestCase):

    def setUp(self):
        self.board = Board()

    def test_validate_hit_valid(self):
        result = self.board.validate_hit(['A', '1'])
        self.assertTrue(result)

    def test_validate_hit_invalid(self):
        # Assuming A1 is already hit
        self.board.hit(['A', '1'])

        result = self.board.validate_hit(['A', '1'])
        self.assertFalse(result)

    def test_generate_computer_hit(self):
        hit = self.board.generate_computer_hit()
        self.assertTrue(self.board.validate_hit(hit))

    def test_generate_computer_hits_nearby(self):
        # Assuming the previous hit was at A1
        previous_hit = ['A', '1']
        hits_nearby = self.board.generate_computer_hits_nearby(previous_hit)
        self.assertTrue(all(self.board.validate_hit(hit) for hit in hits_nearby))

    def test_check_if_won_true(self):
        # Assuming all planes are destroyed
        self.board.place_plane(Plane("N", ['A', '1']))
        self.board.hit(['A', '1'])

        self.assertTrue(self.board.check_if_won())

    def test_check_if_placeable_valid(self):
        plane = Plane("N", ['B', '2'])
        result = self.board.check_if_placeable(plane)
        self.assertTrue(result)


class TestPlane(TestCase):

    def setUp(self):
        # You can set up any necessary objects or states here
        pass

    def test_generate_plane(self):
        plane = Plane("", [])
        plane.generate_plane()

        self.assertIn(plane.orientation, ["N", "S", "E", "W"])
        self.assertIn(plane.position[0], ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])

    def test_check_plane_valid(self):
        plane = Plane("N", ["D", "5"])

        try:
            plane.check_plane()
        except PlaneError as e:
            self.fail(f"Unexpected PlaneError: {e}")

    def test_check_plane_invalid(self):
        # Assuming an invalid plane
        invalid_plane = Plane("N", ["H", "5"])

        with self.assertRaisesRegex(PlaneError, "Invalid Plane Placement ! "):
            invalid_plane.check_plane()

    def test_equality(self):
        plane1 = Plane("N", ["A", "1"])
        plane2 = Plane("N", ["A", "1"])
        plane3 = Plane("S", ["D", "4"])

        self.assertEqual(plane1, plane2)
        self.assertNotEqual(plane1, plane3)


