from duplicated_img_cli import IsDuplicateHashes, IsDuplicateEmbedding
import pytest
import os

FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "test_files"
)


def test_IsDuplicateHashe_self():
    assert IsDuplicateHashes(os.path.join(FIXTURE_DIR, "red1.jpg"), os.path.join(FIXTURE_DIR, "red1.jpg"), 'phash').is_duplicated()

def test_IsDuplicateHashe_simnotdetect():
    assert not IsDuplicateHashes(os.path.join(FIXTURE_DIR, "red1.jpg"), os.path.join(FIXTURE_DIR, "red2.jpg"), 'phash').is_duplicated()

def test_IsDuplicateHashe_notsim():
    assert not IsDuplicateHashes(os.path.join(FIXTURE_DIR, "red1.jpg"), os.path.join(FIXTURE_DIR, "non_dup/1.jpg"), 'phash').is_duplicated()


def test_IsDuplicateEmbedding_self():
    assert IsDuplicateEmbedding(os.path.join(FIXTURE_DIR, "red1.jpg"), os.path.join(FIXTURE_DIR, "red1.jpg"), net='resnet-18', layer='default', thr=0.9).is_duplicated()

def test_IsDuplicateEmbedding_simnotdetect():
    assert IsDuplicateEmbedding(os.path.join(FIXTURE_DIR, "red1.jpg"), os.path.join(FIXTURE_DIR, "red2.jpg"), net='resnet-18', layer='default', thr=0.9).is_duplicated()

def test_IsDuplicateEmbedding_notsim():
    assert not IsDuplicateEmbedding(os.path.join(FIXTURE_DIR, "red1.jpg"), os.path.join(FIXTURE_DIR, "non_dup/1.jpg"), net='resnet-18', layer='default', thr=0.9).is_duplicated()

def test_IsDuplicateEmbedding_notdup():
    assert not IsDuplicateEmbedding(os.path.join(FIXTURE_DIR, "non_dup/1.jpg"), os.path.join(FIXTURE_DIR, "non_dup/2.jpg"), net='resnet-18', layer='default', thr=0.9).is_duplicated()
    assert not IsDuplicateEmbedding(os.path.join(FIXTURE_DIR, "non_dup/1.jpg"), os.path.join(FIXTURE_DIR, "non_dup/3.jpg"), net='resnet-18', layer='default', thr=0.9).is_duplicated()
    assert not IsDuplicateEmbedding(os.path.join(FIXTURE_DIR, "non_dup/1.jpg"), os.path.join(FIXTURE_DIR, "non_dup/4.jpg"), net='resnet-18', layer='default', thr=0.9).is_duplicated()
    assert not IsDuplicateEmbedding(os.path.join(FIXTURE_DIR, "non_dup/1.jpg"), os.path.join(FIXTURE_DIR, "non_dup/5.jpg"), net='resnet-18', layer='default', thr=0.9).is_duplicated()
    assert not IsDuplicateEmbedding(os.path.join(FIXTURE_DIR, "non_dup/2.jpg"), os.path.join(FIXTURE_DIR, "non_dup/3.jpg"), net='resnet-18', layer='default', thr=0.9).is_duplicated()
    assert not IsDuplicateEmbedding(os.path.join(FIXTURE_DIR, "non_dup/2.jpg"), os.path.join(FIXTURE_DIR, "non_dup/4.jpg"), net='resnet-18', layer='default', thr=0.9).is_duplicated()
    assert not IsDuplicateEmbedding(os.path.join(FIXTURE_DIR, "non_dup/2.jpg"), os.path.join(FIXTURE_DIR, "non_dup/5.jpg"), net='resnet-18', layer='default', thr=0.9).is_duplicated()
    assert not IsDuplicateEmbedding(os.path.join(FIXTURE_DIR, "non_dup/3.jpg"), os.path.join(FIXTURE_DIR, "non_dup/4.jpg"), net='resnet-18', layer='default', thr=0.9).is_duplicated()
    assert not IsDuplicateEmbedding(os.path.join(FIXTURE_DIR, "non_dup/3.jpg"), os.path.join(FIXTURE_DIR, "non_dup/5.jpg"), net='resnet-18', layer='default', thr=0.9).is_duplicated()
    assert not IsDuplicateEmbedding(os.path.join(FIXTURE_DIR, "non_dup/4.jpg"), os.path.join(FIXTURE_DIR, "non_dup/5.jpg"), net='resnet-18', layer='default', thr=0.9).is_duplicated()


  
