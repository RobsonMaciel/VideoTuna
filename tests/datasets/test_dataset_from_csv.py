import sys

sys.path.append(".")

import unittest
import os
from src.data.datasets import DatasetFromCSV
import src.data.transforms as transforms


class TestDatasets(unittest.TestCase):

    def test_video_dataset_from_csv(self):
        transform_video = transforms.get_transforms_video()
        if not os.path.exists("src/data/toy_videos"):
            transform_video.transforms[0] = transforms.LoadDummyVideo((100, 100), probs_fail=0.5)
        dataset = DatasetFromCSV(
            "src/data/anno_files/toy_video_dataset.csv",
            "src/data/toy_videos",
            transform={"video": transform_video},
        )
        for i in range(min(5, len(dataset))):
            print(dataset[i].keys())
            self.assertFalse("height" in dataset[i].keys())
            self.assertFalse("width" in dataset[i].keys())
            self.assertGreater(dataset[i]["fps"], 0)

        print(f"len(dataset): {len(dataset)}")
        self.assertEqual(len(dataset), 128)
        self.assertEqual(dataset[0]["video"].shape[2], 256)

        transform_video.transforms[0] = transforms.LoadDummyVideo(probs_fail=0.4)
        dataset = DatasetFromCSV(
            "src/data/anno_files/toy_video_dataset.csv",
            transform={"video": transform_video},
        )
        for i in range(min(5, len(dataset))):
            print(dataset[i].keys())
            self.assertFalse("height" in dataset[i].keys())
            self.assertFalse("width" in dataset[i].keys())
            self.assertGreater(dataset[i]["fps"], 0)

    def test_video_dataset_wo_transforms_from_csv(self):
        dataset = DatasetFromCSV(
            "src/data/anno_files/toy_video_dataset.csv",
            "src/data/toy_videos",
        )
        if not os.path.exists("src/data/toy_videos"):
            transform_video = dataset.transform["video"]
            transform_video.transforms[0] = transforms.LoadDummyVideo(probs_fail=0.5)
            dataset = DatasetFromCSV(
                "src/data/anno_files/toy_video_dataset.csv",
                transform={"video": transform_video},
            )
        for i in range(min(5, len(dataset))):
            print(dataset[i].keys())
            self.assertFalse("height" in dataset[i].keys())
            self.assertFalse("width" in dataset[i].keys())
            self.assertGreater(dataset[i]["fps"], 0)

        print(f"len(dataset): {len(dataset)}")
        self.assertEqual(len(dataset), 128)
        self.assertEqual(dataset[0]["video"].shape[2], 256)

    def test_image_dataset_from_csv(self):
        transform_image = transforms.get_transforms_image()
        if not os.path.exists("src/data/toy_images"):
            transform_image.transforms[0] = transforms.LoadDummyImage(probs_fail=0.5)
        dataset = DatasetFromCSV(
            "src/data/anno_files/toy_image_dataset.csv",
            "src/data/toy_images",
            transform={"image": transform_image},
        )
        for i in range(min(5, len(dataset))):
            print(dataset[i].keys())
            self.assertFalse("height" in dataset[i].keys())
            self.assertFalse("width" in dataset[i].keys())
            self.assertEqual(dataset[i]["fps"], 0)

        print(f"len(dataset): {len(dataset)}")
        self.assertEqual(len(dataset), 16)
        self.assertEqual(dataset[0]["video"].shape[2], 256)

    def test_multi_res(self):
        # Test Video
        transform_video = transforms.get_transforms_video()
        if not os.path.exists("src/data/toy_videos"):
            transform_video.transforms[0] = transforms.LoadDummyVideo(probs_fail=0.5)
        dataset = DatasetFromCSV(
            "src/data/anno_files/toy_video_dataset.csv",
            "src/data/toy_videos",
            transform={"video": transform_video},
            use_multi_res=True,
        )
        for i in range(min(5, len(dataset))):
            print(dataset[i].keys())
            self.assertTrue("height" in dataset[i].keys())
            self.assertTrue("width" in dataset[i].keys())
            self.assertTrue("fps" in dataset[i].keys())

        print(f"len(dataset): {len(dataset)}")
        self.assertEqual(len(dataset), 128)
        self.assertEqual(dataset[0]["video"].shape[2], 256)

        # Test Image
        transform_image = transforms.get_transforms_image()
        if not os.path.exists("src/data/toy_images"):
            transform_image.transforms[0] = transforms.LoadDummyImage(probs_fail=0.5)
        dataset = DatasetFromCSV(
            "src/data/anno_files/toy_image_dataset.csv",
            "src/data/toy_images",
            transform={"image": transform_image},
            use_multi_res=True,
        )
        for i in range(min(5, len(dataset))):
            print(dataset[i].keys())
            self.assertTrue("height" in dataset[i].keys())
            self.assertTrue("width" in dataset[i].keys())
            self.assertEqual(dataset[i]["fps"], 0)

        print(f"len(dataset): {len(dataset)}")
        self.assertEqual(len(dataset), 16)
        self.assertEqual(dataset[0]["video"].shape[2], 256)

    def test_concat_dataset_from_csv(self):
        transform_video = transforms.get_transforms_video()
        if not os.path.exists("src/data/toy_videos"):
            transform_video.transforms[0] = transforms.LoadDummyVideo(probs_fail=0.5)

        transform_image = transforms.get_transforms_image()
        if not os.path.exists("src/data/toy_images"):
            transform_image.transforms[0] = transforms.LoadDummyImage(probs_fail=0.5)
        dataset = DatasetFromCSV(
            [
                "src/data/anno_files/toy_video_dataset.csv",
                "src/data/anno_files/toy_image_dataset.csv",
            ],
            ["src/data/toy_videos", "src/data/toy_images"],
            transform={"video": transform_video, "image": transform_image},
        )
        for i in range(min(5, len(dataset))):
            print(dataset[i].keys())
            self.assertFalse("height" in dataset[i].keys())
            self.assertFalse("width" in dataset[i].keys())
            self.assertTrue("fps" in dataset[i].keys())

        print(f"len(dataset): {len(dataset)}")
        self.assertEqual(len(dataset), 144)
        self.assertEqual(dataset[0]["video"].shape[2], 256)

    def test_anno_wo_meta_info(self):
        transform_video = transforms.get_transforms_video()
        if not os.path.exists("src/data/toy_videos"):
            transform_video.transforms[0] = transforms.LoadDummyVideo(probs_fail=0.5)
        dataset = DatasetFromCSV(
            "src/data/anno_files/toy_video_dataset.csv",
            "src/data/toy_videos",
            transform={"video": transform_video},
            use_multi_res=True,
        )
        data_list = dataset.data_list
        for i, data_item in enumerate(data_list):
            data_list[i] = {"path": data_item["path"], "caption": data_item["caption"]}

        dataset.data_list = data_list
        for i in range(min(5, len(dataset))):
            print(dataset[i].keys())
            self.assertTrue("height" in dataset[i].keys())
            self.assertTrue("width" in dataset[i].keys())
            self.assertTrue("fps" in dataset[i].keys())

        print(f"len(dataset): {len(dataset)}")
        self.assertEqual(len(dataset), 128)
        self.assertEqual(dataset[0]["video"].shape[2], 256)

    def test_anno_wo_meta_info_wo_multi_res(self):
        transform_video = transforms.get_transforms_video()
        if not os.path.exists("src/data/toy_videos"):
            transform_video.transforms[0] = transforms.LoadDummyVideo(probs_fail=0.5)
        dataset = DatasetFromCSV(
            "src/data/anno_files/toy_video_dataset.csv",
            "src/data/toy_videos",
            transform={"video": transform_video},
            use_multi_res=False,
        )
        data_list = dataset.data_list
        for i, data_item in enumerate(data_list):
            data_list[i] = {"path": data_item["path"], "caption": data_item["caption"]}

        dataset.data_list = data_list
        for i in range(min(5, len(dataset))):
            print(dataset[i].keys())
            self.assertFalse("height" in dataset[i].keys())
            self.assertFalse("width" in dataset[i].keys())
            self.assertTrue("fps" in dataset[i].keys())

        print(f"len(dataset): {len(dataset)}")
        self.assertEqual(len(dataset), 128)
        self.assertEqual(dataset[0]["video"].shape[2], 256)

    def test_video_dataset_from_csv_with_split(self):
        transform_video = transforms.get_transforms_video()
        if not os.path.exists("src/data/toy_videos"):
            transform_video.transforms[0] = transforms.LoadDummyVideo(probs_fail=0.5)

        # Test Training Dataset
        train_dataset = DatasetFromCSV(
            "src/data/anno_files/toy_video_dataset.csv",
            "src/data/toy_videos",
            transform={"video": transform_video},
            split_val=True,
        )
        for i in range(min(5, len(train_dataset))):
            print(train_dataset[i].keys())
            self.assertFalse("height" in train_dataset[i].keys())
            self.assertFalse("width" in train_dataset[i].keys())
            self.assertGreater(train_dataset[i]["fps"], 0)

        print(f"len(dataset): {len(train_dataset)}")
        self.assertLessEqual(len(train_dataset), 128)
        self.assertEqual(train_dataset[0]["video"].shape[2], 256)

        # Test Validation Dataset
        val_dataset = DatasetFromCSV(
            "src/data/anno_files/toy_video_dataset.csv",
            "src/data/toy_videos",
            transform={"video": transform_video},
            train=False,
            split_val=True,
        )
        for i in range(min(5, len(val_dataset))):
            print(val_dataset[i].keys())
            self.assertFalse("height" in val_dataset[i].keys())
            self.assertFalse("width" in val_dataset[i].keys())
            self.assertGreater(val_dataset[i]["fps"], 0)

        print(f"len(dataset): {len(val_dataset)}")
        self.assertLessEqual(len(val_dataset), 128)
        self.assertEqual(val_dataset[0]["video"].shape[2], 256)
        # Check if the sum of the lengths of the training and validation datasets is equal to the total number of samples
        self.assertEqual(len(train_dataset) + len(val_dataset), 128)


if __name__ == "__main__":
    unittest.main()
